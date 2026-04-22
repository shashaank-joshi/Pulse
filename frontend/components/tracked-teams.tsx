async function getTrackedTeams() {
  const res = await fetch("http://127.0.0.1:8000/pulse/tracked-teams", {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tracked teams");
  }

  return res.json();
}

export default async function TrackedTeams() {
  const data = await getTrackedTeams();

  return (
    <section className="mb-12">
      <h2 className="text-2xl font-semibold mb-4">Tracked Teams</h2>

      {data.teams.length === 0 ? (
        <p className="text-gray-600">
          No teams tracked yet. Search and track a team to personalize Pulse.
        </p>
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {data.teams.map((team: any) => (
            <div key={team.team_id} className="border rounded-2xl p-4 shadow-sm">
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
            </div>
          ))}
        </div>
      )}
    </section>
  );
}