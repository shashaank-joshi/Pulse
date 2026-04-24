function formatMatchDate(dateString: string) {
  return new Date(dateString).toLocaleString([], {
    dateStyle: "medium",
    timeStyle: "short",
  });
}

async function getRecentTrackedMatches() {
  const res = await fetch("http://127.0.0.1:8000/pulse/tracked-teams/recent", {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch recent tracked matches");
  }

  return res.json();
}

export default async function RecentTrackedMatches() {
  const data = await getRecentTrackedMatches();

  return (
    <section className="mb-12">
      <h2 className="text-2xl font-semibold mb-4">Recent For You</h2>

      {data.matches.length === 0 ? (
        <p className="text-gray-600">
          No recent completed matches found for your tracked teams.
        </p>
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {data.matches.map((match: any) => (
            <div key={match.fixture_id} className="border rounded-2xl p-4 shadow-sm">
              <p className="text-sm text-gray-500">{match.league}</p>
              <p className="font-medium">
                {match.home_team} vs {match.away_team}
              </p>
              <p className="text-sm text-gray-600 mb-1">
                {formatMatchDate(match.date)}
              </p>
              <p className="text-lg">
                {match.home_score ?? "-"} - {match.away_score ?? "-"}
              </p>
              <p className="text-sm text-gray-600">{match.status}</p>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}