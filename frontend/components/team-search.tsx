"use client";

import { useState } from "react";

type TeamResult = {
  team_id: number;
  team_name: string;
  team_logo: string;
  country: string;
};

export default function TeamSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<TeamResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  async function handleSearch() {
    if (!query.trim()) return;

    setLoading(true);
    setError("");
    setMessage("");

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/pulse/teams/search?name=${encodeURIComponent(query)}`,
        { cache: "no-store" }
      );

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Failed to search teams: ${text}`);
      }

      const data = await res.json();
      setResults(data.teams || []);
    } catch (err) {
      console.error(err);
      setError("Could not load team search results.");
      setResults([]);
    } finally {
      setLoading(false);
    }
  }

  async function handleTrackTeam(team: TeamResult) {
    setError("");
    setMessage("");

    try {
      const res = await fetch("http://127.0.0.1:8000/pulse/tracked-teams", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(team),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Failed to track team: ${text}`);
      }

      const data = await res.json();
      setMessage(data.message || "Team tracked successfully.");
    } catch (err) {
      console.error(err);
      setError("Could not track team.");
    }
  }

  return (
    <section className="mb-12">
      <h2 className="text-2xl font-semibold mb-4">Search Teams</h2>

      <div className="flex gap-3 mb-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for a team..."
          className="border rounded-xl px-4 py-2 w-full max-w-md"
        />
        <button
          onClick={handleSearch}
          className="border rounded-xl px-4 py-2 font-medium"
        >
          Search
        </button>
      </div>

      {loading && <p className="text-gray-600">Searching...</p>}
      {error && <p className="text-red-600 mb-2">{error}</p>}
      {message && <p className="text-green-600 mb-2">{message}</p>}

      <div className="grid gap-4 md:grid-cols-2">
        {results.map((team) => (
          <div key={team.team_id} className="border rounded-2xl p-4 shadow-sm">
            <div className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <img
                  src={team.team_logo}
                  alt={team.team_name}
                  className="w-10 h-10 object-contain"
                />
                <div>
                  <p className="font-medium">{team.team_name}</p>
                  <p className="text-sm text-gray-600">{team.country}</p>
                </div>
              </div>

              <button
                onClick={() => handleTrackTeam(team)}
                className="border rounded-xl px-3 py-2 text-sm font-medium"
              >
                Track
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}