import sqlite3
from tools.db_helpers import DB_PATH


def column_exists(cursor, table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    return column_name in columns

def run_migrations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("PRAGMA journal_mode=WAL;")
        cursor.execute("PRAGMA foreign_keys = ON;")

        # ==========================================================
        # Migration 1
        # Add task_id to claims table
        # ==========================================================

        if not column_exists(cursor, "claims", "task_id"):
            cursor.execute("""
                ALTER TABLE claims
                ADD COLUMN task_id TEXT
                REFERENCES tasks(task_id)
                ON DELETE SET NULL;
            """)

            print(" Added claims.task_id")
        else:
            print(" claims.task_id already exists")

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_claims_task_id
            ON claims(task_id);
        """)

        # ==========================================================
        # Migration 2
        # Add session_id to tasks table
        # ==========================================================

        if not column_exists(cursor, "tasks", "session_id"):
            cursor.execute("""
                ALTER TABLE tasks
                ADD COLUMN session_id TEXT
                REFERENCES research_sessions(session_id)
                ON DELETE CASCADE;
            """)

            print(" Added tasks.session_id")
        else:
            print(" tasks.session_id already exists")

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_tasks_session_id
            ON tasks(session_id);
        """)

        # ==========================================================
        # Migration 3
        # Add session_id to claims table
        # ==========================================================

        if not column_exists(cursor, "claims", "session_id"):
            cursor.execute("""
                ALTER TABLE claims
                ADD COLUMN session_id TEXT
                REFERENCES research_sessions(session_id)
                ON DELETE CASCADE;
            """)

            print(" Added claims.session_id")
        else:
            print(" claims.session_id already exists")

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_claims_session_id
            ON claims(session_id);
        """)

        conn.commit()
        print("\n All migrations processed successfully.")

    except Exception as e:
        conn.rollback()
        print(f"\n✗ Migration failed: {e}")
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    run_migrations()