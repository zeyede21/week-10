import React, { useEffect, useState } from 'react';

function App() {
  const [changePoint, setChangePoint] = useState('');

  useEffect(() => {
    fetch("http://localhost:5000/api/change_point")
      .then(res => res.json())
      .then(data => setChangePoint(data.change_point));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Brent Oil Change Point Dashboard</h1>
      <p>Estimated Change Point: <strong>{changePoint}</strong></p>
    </div>
  );
}

export default App;
