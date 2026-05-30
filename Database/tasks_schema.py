import sqlite3
from tools.db_helpers import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA journal_mode=WAL;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (

    task_id TEXT PRIMARY KEY,

    parent_claim TEXT NOT NULL,

    normalized_claim TEXT NOT NULL,

    claim_type TEXT CHECK(
        claim_type IN (
            'factual',
            'causal',
            'predictive',
            'comparative',
            'ethical',
            'vague'
        )
    ),

    classification_confidence REAL CHECK(
        classification_confidence >= 0
        AND classification_confidence <= 1
    ),

    complexity_score REAL CHECK(
        complexity_score >= 0
        AND complexity_score <= 1
    ),

    subproblem_id TEXT NOT NULL,

    subproblem_description TEXT NOT NULL,

    stance_focus TEXT CHECK(
        stance_focus IN (
            'for',
            'against',
            'neutral',
            'both'
        )
    ),

    sources_to_prioritize TEXT,

    search_queries TEXT,

    assigned_agent_id TEXT,

    assumptions_made TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status TEXT DEFAULT 'pending' CHECK(
        status IN (
            'pending',
            'in_progress',
            'completed',
            'failed'
        )
    )

)
""")

# Indexes
cursor.execute("""
ALTER TABLE claims ADD COLUMN task_id TEXT
REFERENCES tasks(task_id) ON DELETE SET NULL;
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_task_status
ON tasks(status);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_assigned_agent
ON tasks(assigned_agent_id);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_claim_type
ON tasks(claim_type);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_subproblem
ON tasks(subproblem_id);
""")

conn.commit()

print("Tasks table created successfully!")

conn.close()