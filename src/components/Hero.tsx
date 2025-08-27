import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { ArrowRight, Download, Code2, Sparkles } from 'lucide-react';

const Hero = () => {
  const skills = ['Gen AI','LLM','Agentic AI', 'MLOPS','TypeScript', 'Python'];

  return (
    <section className="relative min-h-screen flex items-center justify-center px-4 pt-16 overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 bg-gradient-mesh opacity-30"></div>
      <div className="absolute top-20 left-10 w-72 h-72 bg-primary/10 rounded-full blur-3xl floating-element"></div>
      <div className="absolute bottom-20 right-10 w-96 h-96 bg-accent/10 rounded-full blur-3xl floating-element" style={{ animationDelay: '2s' }}></div>
      
      <div className="relative z-10 max-w-6xl mx-auto text-center space-y-12">
        {/* Premium greeting with animated icon */}
        <div className="space-y-4">
          <div className="flex items-center justify-center gap-3 mb-6">
            <div className="relative">
              {/* <Code2 className="w-8 h-8 text-primary pulse-glow" /> */}
              {/* <Sparkles className="w-4 h-4 text-accent absolute -top-1 -right-1 animate-pulse" /> */}
            </div>
            <p className="text-primary font-mono text-xl font-semibold tracking-wide">
              Hellooo, I'm
            </p>
          </div>
          
          <h1 className="text-5xl md:text-8xl gradient-text leading-tight">
            Harshini Vutukuri
          </h1>
          <h2 className="text-2xl md:text-4xl text-muted-foreground font-light tracking-wide">
            <span className="gradient-text-accent"><b>AI/ML</b></span> Developer
            
          </h2 >
          <p className="text-muted-foreground font-light tracking-wide">
          Passionate about building <span className="text-primary font-semibold">scalable applications</span> that solve real-world problems with <br /> Production-Ready <span className="text-primary font-semibold">AI Solutions.</span>
          </p>
        </div>

        {/* Enhanced description */}
        <div className="max-w-3xl mx-auto space-y-6">
          
        </div>

        {/* Skills with enhanced design */}
        <div className="flex flex-wrap justify-center gap-3 stagger-animation">
          {skills.map((skill, index) => (
            <Badge 
              key={skill} 
              variant="secondary" 
              className="px-6 py-3 text-base font-medium bg-card hover:bg-card-hover border border-border-light magnetic-hover cursor-pointer"
              style={{ '--index': index } as React.CSSProperties}
            >
              {skill}
            </Badge>
          ))}
        </div>

        {/* Enhanced code block */}
        <div className="card-elegant max-w-lg mx-auto font-mono text-sm md:text-base text-left group cursor-pointer card-hover">
          <div className="absolute top-4 right-4 flex gap-2">
            <div className="w-3 h-3 bg-destructive rounded-full"></div>
            <div className="w-3 h-3 bg-accent rounded-full"></div>
            <div className="w-3 h-3 bg-primary rounded-full pulse-glow"></div>
          </div>
          
          <div className="text-muted-foreground mb-4 text-xs uppercase tracking-wider">
            // Current status
          </div>
          
          <div className="text-foreground space-y-1">
            <div>
              <span className="text-accent">const</span>{' '}
              <span className="text-primary"> developer</span> = {'{'}<br />
            </div>
            <div className="ml-4">
              <span className="text-accent">name</span>: <span className="text-primary">"Harshini"</span>,<br />
              <span className="text-accent">role</span>: <span className="text-primary">"AI/ML Developer"</span>,<br />
              <span className="text-accent">experience</span>: <span className="text-primary">"1.8+ years"</span>,<br />
              <span className="text-accent">available</span>: <span className="text-primary">true</span><br />
            </div>
            <div>{'};'}</div>
          </div>
          
          <div className="mt-4 text-xs text-muted-foreground opacity-0 group-hover:opacity-100 transition-opacity">
            <b><i>Click to explore my work →</i></b>
          </div>
        </div>

        {/* Enhanced CTA buttons */}
        <div className="flex flex-col sm:flex-row gap-6 justify-center">
        <a
  href="https://github.com/Harshin1V?tab=repositories"
  target="_blank"
  rel="noopener noreferrer"
>
  <Button size="lg" className="px-8 py-4 text-lg glow-effect magnetic-hover group">
    <span className="group-hover:scale-110 transition-transform">View My Work</span>
    <ArrowRight className="ml-3 h-5 w-5 group-hover:translate-x-1 transition-transform" />
  </Button>
</a>

          <a
  href="https://drive.google.com/file/d/1uxaxbrfIeMTlNp8_JobUwU3PPNEC3fAG/view"
  target="_blank"
  rel="noopener noreferrer"
>
  <Button
    variant="outline"
    size="lg"
    className="px-8 py-4 text-lg border-border-light hover:border-primary hover:text-primary magnetic-hover group"
  >
    <Download className="mr-3 h-5 w-5 group-hover:scale-110 transition-transform" />
    <span>Download Resume</span>
  </Button>
</a>

        </div>

        {/* Enhanced scroll indicator */}
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2">
          <div className="flex flex-col items-center gap-2 animate-bounce">
            <div className="text-xs text-muted-foreground font-mono tracking-wider uppercase">
              Scroll Down
            </div>
            <div className="w-8 h-12 border-2 border-primary rounded-full flex justify-center relative overflow-hidden">
              <div className="w-1 h-3 bg-primary rounded-full mt-2 animate-pulse pulse-glow"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;