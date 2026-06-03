#!/usr/bin/env python3
"""
Database Initialization Script
Run this to create and initialize the database
"""

import sqlite3
import os
from pathlib import Path

def get_db_path():
    """Get database path"""
    return Path(__file__).parent / 'churn.db'

def run_migration(cursor, migration_file):
    """Run a single migration file"""
    with open(migration_file, 'r') as f:
        sql = f.read()
        try:
            cursor.executescript(sql)
            print(f"✅ Ran migration: {migration_file.name}")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error in {migration_file.name}: {e}")
            return False

def run_seed(cursor, seed_file):
    """Run a single seed file"""
    with open(seed_file, 'r') as f:
        sql = f.read()
        try:
            cursor.executescript(sql)
            print(f"✅ Seeded data: {seed_file.name}")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error in {seed_file.name}: {e}")
            return False

def init_database():
    """Initialize the database with all migrations and seeds"""
    db_path = get_db_path()
    
    # Remove existing database if it exists
    if db_path.exists():
        os.remove(db_path)
        print("🗑️ Removed existing database")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\n📦 Running migrations...")
    print("-" * 40)
    
    # Run migrations in order
    migrations_dir = Path(__file__).parent / 'migrations'
    migration_files = sorted(migrations_dir.glob('*.sql'))
    
    for migration_file in migration_files:
        run_migration(cursor, migration_file)
    
    print("\n🌱 Seeding data...")
    print("-" * 40)
    
    # Run seeds
    seeds_dir = Path(__file__).parent / 'seeds'
    seed_files = sorted(seeds_dir.glob('*.sql'))
    
    for seed_file in seed_files:
        run_seed(cursor, seed_file)
    
    # Commit changes
    conn.commit()
    
    # Verify database
    print("\n🔍 Verifying database...")
    print("-" * 40)
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables created: {len(tables)}")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Get counts
    cursor.execute("SELECT COUNT(*) FROM customers")
    customer_count = cursor.fetchone()[0]
    print(f"\nCustomers: {customer_count}")
    
    cursor.execute("SELECT COUNT(*) FROM retention_strategies")
    strategy_count = cursor.fetchone()[0]
    print(f"Retention Strategies: {strategy_count}")
    
    cursor.execute("SELECT COUNT(*) FROM simulations")
    simulation_count = cursor.fetchone()[0]
    print(f"Simulations: {simulation_count}")
    
    # Close connection
    conn.close()
    
    print("\n" + "="*50)
    print("✅ Database initialized successfully!")
    print(f"📁 Database location: {db_path}")
    print("="*50)

if __name__ == "__main__":
    init_database()