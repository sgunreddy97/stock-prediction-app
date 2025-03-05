import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import axios from "axios";

const Predictions = () => {
    const [predictions, setPredictions] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/predictions/AAPL/predict?days=30")
            .then(response => setPredictions(response.data.predictions))
            .catch(error => console.error("Error fetching predictions:", error));
    }, []);

    return (
        <>
            <Navbar />
            <h1>Predictions</h1>
            <ul>
                {predictions.map((price, index) => (
                    <li key={index}>Day {index + 1}: ${price.toFixed(2)}</li>
                ))}
            </ul>
        </>
    );
};

export default Predictions;
