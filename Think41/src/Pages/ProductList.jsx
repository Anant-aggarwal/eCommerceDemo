import { Link } from 'react-router-dom';
import { products } from '../data/products';

export default function ProductList() {
  return (
    <div className="container">
      <h2>Product List</h2>
      <div className="grid">
        {products.map((p) => (
          <Link to={`/products/${p.id}`} key={p.id} className="card">
            <h3>{p.name}</h3>
            <p><strong>Brand:</strong> {p.brand}</p>
            <p><strong>Price:</strong> ${p.retail_price}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
