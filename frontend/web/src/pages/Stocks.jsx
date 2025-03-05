import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import StockCard from "../components/StockCard";
import axios from "axios";

const Stocks = () => {
    const [stocks, setStocks] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/stocks/AAPL/technical")
            .then(response => setStocks([response.data]))
            .catch(error => console.error("Error fetching stocks:", error));
    }, []);

    return (
        <>
            <Navbar />
            <h1>Stocks</h1>
            <div className="stocks-container">
                {stocks.map((stock, index) => <StockCard key={index} stock={stock} />)}
            </div>
        </>
    );
};

export default Stocks;
