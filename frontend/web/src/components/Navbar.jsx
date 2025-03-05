import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar">
            <h2>Stock Predictor</h2>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/stocks">Stocks</Link></li>
                <li><Link to="/predictions">Predictions</Link></li>
            </ul>
        </nav>
    );
};

export default Navbar;
