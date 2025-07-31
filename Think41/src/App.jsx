import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ProductList from './Pages/ProductList';
import ProductDetail from './Pages/ProductDetail';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/products/:id" element={<ProductDetail />} />
      </Routes>
    </Router>
  );
}
