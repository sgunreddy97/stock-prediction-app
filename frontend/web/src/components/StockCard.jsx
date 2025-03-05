const StockCard = ({ stock }) => {
    return (
        <div className="stock-card">
            <h3>{stock.ticker}</h3>
            <p>Price: ${stock.price}</p>
            <p>Sentiment: {stock.sentiment > 0 ? "Bullish 📈" : "Bearish 📉"}</p>
        </div>
    );
};

export default StockCard;
