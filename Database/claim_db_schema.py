import sqlite3
from tools.db_helpers import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA journal_mode=WAL;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS claims (

    claim_id TEXT PRIMARY KEY,

    raw_text TEXT NOT NULL,
    normalized_claim TEXT NOT NULL,

    source_url TEXT,
    source_domain TEXT,

    source_type TEXT CHECK(
        source_type IN (
            'academic',
            'news',
            'social',
            'government',
            'blog',
            'other'
        )
    ),

    source_published_date TEXT,
    claim_date TEXT,

    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    agent_id TEXT NOT NULL,

    stance TEXT CHECK(
        stance IN (
            'for',
            'against',
            'neutral',
            'contextual'
        )
    ),

    verdict_relevance_score REAL CHECK(
        verdict_relevance_score >= 0
        AND verdict_relevance_score <= 1
    ),

    duplicate_similarity_score REAL CHECK(
        duplicate_similarity_score >= 0
        AND duplicate_similarity_score <= 1
    ),

    confidence_score REAL CHECK(
        confidence_score >= 0
        AND confidence_score <= 1
    ),

    flags TEXT,

    verification_status TEXT DEFAULT 'unverified' CHECK(
        verification_status IN (
            'unverified',
            'verified',
            'disputed',
            'rejected'
        )
    ),

    parent_claim_id TEXT,

    FOREIGN KEY(parent_claim_id)
        REFERENCES claims(claim_id)
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_stance ON claims(stance);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_verification_status ON claims(verification_status);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_source_domain ON claims(source_domain);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_agent_id ON claims(agent_id);")

conn.commit()
print("Claims table created successfully!")
conn.close()