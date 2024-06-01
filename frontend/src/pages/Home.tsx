import "bootstrap/dist/css/bootstrap.min.css";
import "./CSS/Home.css";

import {
  Container,
  Row,
  Col,
  Button,
  Alert,
  Breadcrumb,
  Card,
  Form,
} from "react-bootstrap";

const Home = () => {
  return (
    <div className="HomePage">
      <h1>Documents Managment Project (DMP) - React Web Client</h1>
      <h1>Home Page</h1>
      <div>
        <p>
          Secure simple, and easy to use documents managment solution. We
          develop custom version of your documents and allow you to focus on
          clients.
        </p>
      </div>
      <div>
        <p>Email, sign up, sign in with your personal email account.</p>
      </div>

      <div>
        <p>DMP is available on the app, Android </p>
      </div>
    </div>
  );
};

export default Home;
