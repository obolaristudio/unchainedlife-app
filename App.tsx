import Hero from './components/Hero';
import Features from './components/Features';
import SocialProof from './components/SocialProof';
import WaitlistForm from './components/WaitlistForm';
import Footer from './components/Footer';

function App() {
  const scrollToWaitlist = () => {
    document.getElementById('waitlist')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen">
      <Hero onCTAClick={scrollToWaitlist} />
      <Features />
      <SocialProof />
      <WaitlistForm />
      <Footer />
    </div>
  );
}

export default App;
