import { useState, FormEvent } from 'react';
import { Mail, CheckCircle, AlertCircle, Loader } from 'lucide-react';
import { supabase } from '../lib/supabase';

export default function WaitlistForm() {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setStatus('loading');
    setMessage('');

    try {
      const { error } = await supabase
        .from('waitlist')
        .insert([{ email, source: 'landing_page' }]);

      if (error) {
        if (error.code === '23505') {
          setStatus('error');
          setMessage('Este email já está cadastrado na lista de espera.');
        } else {
          throw error;
        }
      } else {
        setStatus('success');
        setMessage('Parabéns! Você está na lista de espera. Em breve entraremos em contato.');
        setEmail('');
      }
    } catch (error) {
      setStatus('error');
      setMessage('Algo deu errado. Por favor, tente novamente.');
      console.error('Error signing up:', error);
    }
  };

  return (
    <section id="waitlist" className="py-24 bg-gradient-to-br from-purple-900 via-blue-900 to-purple-800 relative overflow-hidden">
      <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PHBhdGggZD0iTTM2IDM0djItaDJ2LTJoLTJ6bTAgNGgydjJoLTJ2LTJ6bS0yIDJoLTJ2Mmgydi0yem0tMiAwaC0ydjJoMnYtMnptLTItMmgtMnYyaDJ2LTJ6bTItMmgydi0yaC0ydjJ6bTAtMmgydi0yaC0ydjJ6bTItMmgydi0yaC0ydjJ6Ii8+PC9nPjwvZz48L3N2Zz4=')] opacity-20"></div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 className="text-4xl sm:text-5xl font-bold text-white mb-6">
          Comece sua jornada de <span className="text-blue-300">liberdade</span> hoje
        </h2>
        <p className="text-xl text-blue-100 mb-12 max-w-2xl mx-auto">
          Inscreva-se agora e seja um dos primeiros a ter acesso ao Unchained Life quando lançarmos
        </p>

        <form onSubmit={handleSubmit} className="max-w-md mx-auto">
          <div className="flex flex-col sm:flex-row gap-4 mb-6">
            <div className="flex-1 relative">
              <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="seu@email.com"
                required
                disabled={status === 'loading'}
                className="w-full pl-12 pr-4 py-4 rounded-full border-2 border-white/20 bg-white/10 backdrop-blur-sm text-white placeholder-white/60 focus:outline-none focus:border-blue-300 focus:bg-white/20 transition-all disabled:opacity-50"
              />
            </div>
            <button
              type="submit"
              disabled={status === 'loading'}
              className="px-8 py-4 bg-white text-purple-900 rounded-full font-semibold hover:bg-blue-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap"
            >
              {status === 'loading' ? (
                <span className="flex items-center justify-center">
                  <Loader className="w-5 h-5 animate-spin" />
                </span>
              ) : (
                'Entrar na lista'
              )}
            </button>
          </div>

          {status === 'success' && (
            <div className="flex items-center justify-center gap-2 text-green-300 bg-green-900/30 backdrop-blur-sm p-4 rounded-xl border border-green-500/30">
              <CheckCircle className="w-5 h-5 flex-shrink-0" />
              <p className="text-sm">{message}</p>
            </div>
          )}

          {status === 'error' && (
            <div className="flex items-center justify-center gap-2 text-red-300 bg-red-900/30 backdrop-blur-sm p-4 rounded-xl border border-red-500/30">
              <AlertCircle className="w-5 h-5 flex-shrink-0" />
              <p className="text-sm">{message}</p>
            </div>
          )}
        </form>

        <p className="mt-8 text-sm text-blue-200">
          Seus dados estão seguros. Nunca compartilharemos seu email com terceiros.
        </p>
      </div>
    </section>
  );
}
