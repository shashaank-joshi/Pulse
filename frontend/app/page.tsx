async function getFavorites() {
  const res = await fetch("http://127.0.0.1:8000/favorites", {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch favorites");
  }

  return res.json();
}

export default async function Home() {
  const data = await getFavorites();

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

        <section className="mb-10">
          <h2 className="text-2xl font-semibold mb-4">Favorites</h2>
          <div className="grid gap-4 md:grid-cols-2">
            {data.favorites.map((item: { id: number; category: string; name: string }) => (
              <div key={item.id} className="border rounded-2xl p-4 shadow-sm">
                <p className="text-sm text-gray-500 uppercase">{item.category}</p>
                <p className="text-lg font-medium">{item.name}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="grid gap-6 md:grid-cols-3">
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