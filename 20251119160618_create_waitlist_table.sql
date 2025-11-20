/*
  # Create waitlist table for Unchained Life

  1. New Tables
    - `waitlist`
      - `id` (uuid, primary key) - Unique identifier for each signup
      - `email` (text, unique) - User's email address
      - `created_at` (timestamptz) - Timestamp of signup
      - `source` (text) - Optional field to track where signup came from
  
  2. Security
    - Enable RLS on `waitlist` table
    - Add policy for public insert access (anyone can sign up)
    - No read policies (admin only access via service role)
  
  3. Notes
    - Email is unique to prevent duplicate signups
    - Created_at defaults to current timestamp
    - Source field can track marketing campaigns or referrals
*/

CREATE TABLE IF NOT EXISTS waitlist (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text UNIQUE NOT NULL,
  created_at timestamptz DEFAULT now(),
  source text DEFAULT 'landing_page'
);

ALTER TABLE waitlist ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can sign up for waitlist"
  ON waitlist
  FOR INSERT
  TO anon
  WITH CHECK (true);