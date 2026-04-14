export default function Home() {
  return (
    <main className="min-h-screen bg-white text-black px-8 py-12">
      <div className="max-w-5xl mx-auto">
        <header className="mb-10">
          <h1 className="text-5xl font-bold mb-4">Pulse</h1>
          <p className="text-lg text-gray-700 max-w-2xl">
            A personal sports and music intelligence platform to track favorites,
            save notes and trivia, and generate useful summaries from structured
            data.
          </p>
        </header>

        <section className="grid gap-6 md:grid-cols-2">
          <div className="border rounded-2xl p-6 shadow-sm">
            <h2 className="text-2xl font-semibold mb-3">Favorites</h2>
            <p className="text-gray-600">
              Track favorite teams, players, artists, songs, and genres in one place.
            </p>
          </div>

          <div className="border rounded-2xl p-6 shadow-sm">
            <h2 className="text-2xl font-semibold mb-3">Recent Updates</h2>
            <p className="text-gray-600">
              View the latest football updates and saved music discoveries.
            </p>
          </div>

          <div className="border rounded-2xl p-6 shadow-sm">
            <h2 className="text-2xl font-semibold mb-3">Notes & Trivia</h2>
            <p className="text-gray-600">
              Save random TILs, observations, and personal notes across sports and music.
            </p>
          </div>

          <div className="border rounded-2xl p-6 shadow-sm">
            <h2 className="text-2xl font-semibold mb-3">AI Summary</h2>
            <p className="text-gray-600">
              Generate simple summaries from your saved notes and tracked updates.
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}