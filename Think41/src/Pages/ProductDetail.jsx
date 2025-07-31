import { useParams, Link } from 'react-router-dom';
import { products } from '../data/products';

export default function ProductDetail() {
  const { id } = useParams();
  const product = products.find(p => p.id === parseInt(id));

  if (!product) return <p>Product not found.</p>;

  return (
    <div className="container">
      <h2>{product.name}</h2>
      <p><strong>Brand:</strong> {product.brand}</p>
      <p><strong>Category:</strong> {product.category}</p>
      <p><strong>Cost:</strong> ${product.cost}</p>
      <p><strong>Retail Price:</strong> ${product.retail_price}</p>
      <Link to="/">← Back to list</Link>
    </div>
  );
}
