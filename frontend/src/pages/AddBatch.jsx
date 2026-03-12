import { useState } from "react";
import API from "../services/api";

function AddBatch() {

  const [batchId, setBatchId] = useState("");
  const [fuelType, setFuelType] = useState("");
  const [producer, setProducer] = useState("");
  const [carbonEmission, setCarbonEmission] = useState("");
  const [txHash, setTxHash] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/add-batch", {
        batch_id: batchId,
        fuel_type: fuelType,
        producer: producer,
        carbon_emission: carbonEmission
      });

      setTxHash(res.data.blockchain_tx);

      alert("Batch Added Successfully!");

    } catch (error) {
      console.error(error);
      alert("Error adding batch");
    }
  };

  return (
    <div style={{padding:20}}>

      <h2>Add Fuel Batch</h2>

      <form onSubmit={handleSubmit}>

        <input
          placeholder="Batch ID"
          onChange={(e) => setBatchId(e.target.value)}
        />

        <br/><br/>

        <input
          placeholder="Fuel Type"
          onChange={(e) => setFuelType(e.target.value)}
        />

        <br/><br/>

        <input
          placeholder="Producer"
          onChange={(e) => setProducer(e.target.value)}
        />

        <br/><br/>

        <input
          placeholder="Carbon Emission"
          onChange={(e) => setCarbonEmission(e.target.value)}
        />

        <br/><br/>

        <button>Add Batch</button>

      </form>

      {txHash && (
        <div style={{marginTop:20}}>
          <b>Blockchain Transaction Hash:</b>
          <p>{txHash}</p>
        </div>
      )}

    </div>
  );
}

export default AddBatch;