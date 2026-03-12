import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import AddBatch from "./pages/AddBatch";
import TrackFuel from "./pages/TrackFuel";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />
        <Route path="/add-batch" element={<AddBatch />} />
        <Route path="/track" element={<TrackFuel />} />

      </Routes>

    </BrowserRouter>

  );
}

export default App;