import sqlite3
from tools.db_helpers import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA journal_mode=WAL;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS verifications (

    verification_id TEXT PRIMARY KEY,

    claim_id TEXT NOT NULL,

    verified_by TEXT NOT NULL,

    verified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    source_credibility_score REAL CHECK(
        source_credibility_score >= 0
        AND source_credibility_score <= 1
    ),

    corroborating_sources_count INTEGER CHECK(
        corroborating_sources_count >= 0
    ),

    source_diversity_score REAL CHECK(
        source_diversity_score >= 0
        AND source_diversity_score <= 1
    ),

    consistency_score REAL CHECK(
        consistency_score >= 0
        AND consistency_score <= 1
    ),

    is_contradicted INTEGER CHECK(
        is_contradicted IN (0, 1)
    ),

    contradiction_score REAL CHECK(
        contradiction_score >= 0
        AND contradiction_score <= 1
    ),

    timeline_score REAL CHECK(
        timeline_score >= 0
        AND timeline_score <= 1
    ),

    is_outdated INTEGER CHECK(
        is_outdated IN (0, 1)
    ),

    verification_confidence REAL CHECK(
        verification_confidence >= 0
        AND verification_confidence <= 1
    ),

    verification_method TEXT,

    reasoning_summary TEXT,

    final_verdict TEXT CHECK(
        final_verdict IN (
            'verified',
            'disputed',
            'rejected',
            'insufficient_evidence'
        )
    ),

    FOREIGN KEY(claim_id)
        REFERENCES claims(claim_id)
        ON DELETE CASCADE

)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_verification_claim_id
ON verifications(claim_id);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_final_verdict
ON verifications(final_verdict);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_verified_by
ON verifications(verified_by);
""")

conn.commit()
print("Verification table created successfully!")
conn.close()