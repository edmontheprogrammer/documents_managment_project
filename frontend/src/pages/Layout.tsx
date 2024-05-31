import { Outlet, Link } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./CSS/Layout.css";

import {
  Container,
  Row,
  Col,
  Button,
  Alert,
  Breadcrumb,
  BreadcrumbItem,
  Card,
  Form,
} from "react-bootstrap";

const Layout = () => {
  return (
    <div className="LayOutPage">
      {/* <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/contact">Contact</Link>
          </li>
        </ul>
      </nav> */}

      <div className="container-fluid">
        <nav className="navbar navbar-expand-lg bg-light">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              CMP
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNavDropdown"
              aria-controls="navbarNavDropdown"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavDropdown">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/contact">
                    Contact
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
