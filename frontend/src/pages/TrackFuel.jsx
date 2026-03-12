import { useState } from "react";
import API from "../services/api";

function TrackFuel() {

  const [batchId, setBatchId] = useState("");
  const [data, setData] = useState(null);

  const trackBatch = async () => {

    try {
      const res = await API.get(`/track-batch/${batchId}`);
      setData(res.data);
    }
    catch (error) {
      alert("Batch not found");
    }

  };

  return (
    <div style={{padding:20}}>

      <h2>Track Fuel Batch</h2>

      <input
        placeholder="Enter Batch ID"
        onChange={(e) => setBatchId(e.target.value)}
      />

      <button onClick={trackBatch}>Track</button>

      {data && (
        <div style={{marginTop:20}}>

          <h3>Batch Details</h3>

          <p><b>Batch ID:</b> {data.batch_id}</p>
          <p><b>Fuel Type:</b> {data.fuel_type}</p>
          <p><b>Producer:</b> {data.producer}</p>
          <p><b>Carbon Emission:</b> {data.carbon_emission}</p>
          <p><b>Status:</b> {data.status}</p>

        </div>
      )}

    </div>
  );
}

export default TrackFuel;