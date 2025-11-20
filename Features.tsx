import { Bot, Calendar, Users, Shield, Heart, TrendingUp } from 'lucide-react';

const features = [
  {
    icon: Bot,
    title: 'Suporte com IA 24/7',
    description: 'Assistente inteligente que entende suas lutas e oferece apoio personalizado a qualquer momento, sem julgamentos.',
  },
  {
    icon: Calendar,
    title: 'Jornada de 90 dias',
    description: 'Programa estruturado e comprovado que te guia passo a passo através da transformação completa.',
  },
  {
    icon: Users,
    title: 'Comunidade anônima',
    description: 'Conecte-se com outros que compartilham a mesma jornada em um ambiente seguro e confidencial.',
  },
  {
    icon: Heart,
    title: 'Princípios cristãos',
    description: 'Encontre força na fé com recursos bíblicos, orações e encorajamento espiritual diário.',
  },
  {
    icon: Shield,
    title: 'Privacidade total',
    description: 'Seus dados são protegidos com criptografia de ponta. Ninguém precisa saber da sua jornada.',
  },
  {
    icon: TrendingUp,
    title: 'Progresso rastreado',
    description: 'Visualize sua evolução, celebre vitórias e identifique padrões para fortalecer sua recuperação.',
  },
];

export default function Features() {
  return (
    <section className="py-24 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
            Ferramentas para sua <span className="bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">liberdade</span>
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Tudo o que você precisa para vencer o vício e reconstruir sua vida
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <div
                key={index}
                className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1 border border-gray-100"
              >
                <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-blue-500 rounded-xl flex items-center justify-center mb-6">
                  <Icon className="w-7 h-7 text-white" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{feature.title}</h3>
                <p className="text-gray-600 leading-relaxed">{feature.description}</p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
