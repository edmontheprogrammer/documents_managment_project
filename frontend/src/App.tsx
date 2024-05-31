import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

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

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
import About from "./pages/About";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
