import { Heart } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h3 className="text-2xl font-bold mb-2">Unchained Life</h3>
          <p className="text-gray-400 mb-6">Quebre as correntes. Viva livre.</p>

          <div className="flex items-center justify-center gap-2 text-gray-400 text-sm">
            <span>Feito com</span>
            <Heart className="w-4 h-4 text-red-500 fill-red-500" />
            <span>para ajudar vidas</span>
          </div>

          <div className="mt-8 pt-8 border-t border-gray-800">
            <p className="text-gray-500 text-sm">
              © {new Date().getFullYear()} Unchained Life. Todos os direitos reservados.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
