import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <div style={{ padding: 40 }}>

      <h1>Green Fuel Supply Chain</h1>
      <p>Blockchain-Based Tracking System</p>

      <div style={{ marginTop: 30 }}>

        <Link to="/add-batch">
          <button style={{ marginRight: 20 }}>Add Fuel Batch</button>
        </Link>

        <Link to="/track">
          <button>Track Fuel Batch</button>
        </Link>

      </div>

    </div>
  );
}

export default Dashboard;