import { Star, Quote } from 'lucide-react';

const testimonials = [
  {
    name: 'Rafael S.',
    role: '45 dias livre',
    content: 'Pela primeira vez em anos, sinto que tenho controle sobre minha vida. O apoio da IA me ajuda nos momentos mais difíceis.',
    rating: 5,
  },
  {
    name: 'Lucas M.',
    role: '90 dias livre',
    content: 'A jornada de 90 dias mudou minha vida. Restaurei meu relacionamento com Deus e minha família. Valeu cada dia.',
    rating: 5,
  },
  {
    name: 'Pedro A.',
    role: '30 dias livre',
    content: 'Tentei sozinho por anos. A comunidade anônima e o suporte 24/7 fizeram toda a diferença. Não estou mais sozinho nessa.',
    rating: 5,
  },
];

const stats = [
  { value: '87%', label: 'Taxa de sucesso após 90 dias' },
  { value: '5.000+', label: 'Vidas transformadas' },
  { value: '24/7', label: 'Suporte disponível' },
  { value: '100%', label: 'Anônimo e seguro' },
];

export default function SocialProof() {
  return (
    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
            Vidas sendo <span className="bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">transformadas</span>
          </h2>
          <p className="text-xl text-gray-600">
            Junte-se a milhares que já começaram sua jornada de liberdade
          </p>
        </div>

        <div className="grid md:grid-cols-4 gap-8 mb-20">
          {stats.map((stat, index) => (
            <div key={index} className="text-center">
              <div className="text-4xl sm:text-5xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent mb-2">
                {stat.value}
              </div>
              <div className="text-gray-600 font-medium">{stat.label}</div>
            </div>
          ))}
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <div
              key={index}
              className="bg-gradient-to-br from-purple-50 to-blue-50 p-8 rounded-2xl border border-purple-100 hover:shadow-lg transition-shadow"
            >
              <Quote className="w-10 h-10 text-purple-400 mb-4" />
              <div className="flex gap-1 mb-4">
                {[...Array(testimonial.rating)].map((_, i) => (
                  <Star key={i} className="w-5 h-5 fill-yellow-400 text-yellow-400" />
                ))}
              </div>
              <p className="text-gray-700 mb-6 leading-relaxed italic">"{testimonial.content}"</p>
              <div>
                <div className="font-semibold text-gray-900">{testimonial.name}</div>
                <div className="text-sm text-purple-600 font-medium">{testimonial.role}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
