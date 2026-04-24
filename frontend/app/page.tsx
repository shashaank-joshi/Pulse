import TrackedTeams from "../components/tracked-teams";
import UpcomingTrackedMatches from "../components/upcoming-tracked-matches";
import TeamSearch from "../components/team-search";

async function getLiveMatches() {
  const res = await fetch("http://127.0.0.1:8000/pulse/live", {
    cache: "no-store",
  });

  if (!res.ok) throw new Error("Failed to fetch live matches");
  return res.json();
}

async function getTodayFixtures() {
  const today = new Date().toISOString().split("T")[0];

  const res = await fetch(
    `http://127.0.0.1:8000/pulse/fixtures/date?date=${today}`,
    { cache: "no-store" }
  );

  if (!res.ok) throw new Error("Failed to fetch today's fixtures");
  return res.json();
}

export default async function Home() {
  const [liveData, fixturesData] = await Promise.all([
    getLiveMatches(),
    getTodayFixtures(),
  ]);

  return (
    <main className="min-h-screen bg-white text-black px-8 py-12">
      <div className="max-w-6xl mx-auto">
        <header className="mb-10">
          <h1 className="text-5xl font-bold mb-4">Pulse</h1>
          <p className="text-lg text-gray-700 max-w-3xl">
            A personalized sports and culture intelligence platform that helps
            users track teams, artists, and topics they care about, then
            delivers live context, recent developments, and discovery in one place.
          </p>
        </header>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Live Now</h2>
          <div className="grid gap-4 md:grid-cols-2">
            {liveData.matches.slice(0, 4).map((match: any) => (
              <div key={match.fixture_id} className="border rounded-2xl p-4 shadow-sm">
                <p className="text-sm text-gray-500">{match.league}</p>
                <p className="font-medium">
                  {match.home_team} vs {match.away_team}
                </p>
                <p className="text-lg">
                  {match.home_score} - {match.away_score}
                </p>
                <p className="text-sm text-gray-600">
                  {match.status} {match.elapsed ? `• ${match.elapsed}'` : ""}
                </p>
              </div>
            ))}
          </div>
        </section>

        <TrackedTeams />

        <UpcomingTrackedMatches />

        <TeamSearch />

        <section>
          <h2 className="text-2xl font-semibold mb-4">Today&apos;s Matches</h2>
          <div className="grid gap-4 md:grid-cols-2">
            {fixturesData.matches.slice(0, 6).map((match: any) => (
              <div key={match.fixture_id} className="border rounded-2xl p-4 shadow-sm">
                <p className="text-sm text-gray-500">{match.league}</p>
                <p className="font-medium">
                  {match.home_team} vs {match.away_team}
                </p>
                <p className="text-lg">
                  {match.home_score ?? "-"} - {match.away_score ?? "-"}
                </p>
                <p className="text-sm text-gray-600">{match.status}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}