const hre = require("hardhat");

async function main() {

  // Get contract factory
  const GreenFuel = await hre.ethers.getContractFactory("GreenFuel");

  console.log("Deploying GreenFuel contract...");

  // Deploy contract
  const greenFuel = await GreenFuel.deploy();

  // Wait until deployment finishes
  await greenFuel.waitForDeployment();

  // Print contract address
  console.log("GreenFuel deployed to:", await greenFuel.getAddress());

}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });