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

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <Container fluid>
//           <Form>
//             <Row>
//               <Col md>
//                 <Form.Group controlId="formEmail">
//                   <Form.Label>Email Address</Form.Label>
//                   <Form.Control type="email" placeholder="Example@email.com" />
//                   <Form.Text className="text-muted">
//                     We'll Never share your email address, trust us!
//                   </Form.Text>
//                 </Form.Group>
//               </Col>
//               <Col md>
//                 <Form.Group controlId="formPassword">
//                   <Form.Label>Password</Form.Label>
//                   <Form.Control type="password" placeholder="Password" />
//                 </Form.Group>
//               </Col>
//             </Row>
//             <Button variant="secondary">Login</Button>
//           </Form>

//           <Card className="mb-3" style={{ color: "#000" }}>
//             <Card.Img src="https://picsum.photos/id/237/200/50" />
//             <Card.Body>
//               <Card.Title>Card Example</Card.Title>
//               <Card.Text>This is an example of react bootstrap cards</Card.Text>
//               <Button variant="primary">Read More</Button>
//             </Card.Body>
//           </Card>
//           <Breadcrumb>
//             <Breadcrumb.Item>Test </Breadcrumb.Item>
//             <Breadcrumb.Item> Test 2</Breadcrumb.Item>
//             <Breadcrumb.Item active> Test 3</Breadcrumb.Item>
//           </Breadcrumb>
//           <Alert variant="success"> This is a button</Alert>
//           <Button>Test Button</Button>
//         </Container>
//       </header>
//     </div>
//   );
// }

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
