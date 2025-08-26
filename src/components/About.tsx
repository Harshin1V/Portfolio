import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { Code, Database, Palette, Zap } from 'lucide-react';

const About = () => {
  const skills = {
    frontend: ['React', 'Vue.js', 'TypeScript', 'Tailwind CSS', 'Next.js', 'Vite'],
    backend: ['Node.js', 'Python', 'Express', 'FastAPI', 'PostgreSQL', 'MongoDB'],
    tools: ['Git', 'Docker', 'AWS', 'Vercel', 'Figma', 'VS Code']
  };

  const highlights = [
    {
      icon: Code,
      title: 'Clean Code',
      description: 'Writing maintainable, scalable code with modern best practices'
    },
    {
      icon: Zap,
      title: 'Performance',
      description: 'Optimizing applications for speed and user experience'
    },
    {
      icon: Database,
      title: 'Full Stack',
      description: 'End-to-end development from database to deployment'
    },
    {
      icon: Palette,
      title: 'Design',
      description: 'Creating beautiful, intuitive user interfaces'
    }
  ];

  return (
    <section id="about" className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            About <span className="gradient-text">Me</span>
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Passionate developer with 5+ years of experience building web applications.
            I love turning complex problems into simple, beautiful solutions.
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-12 mb-16">
          {/* Story */}
          <div className="space-y-6">
            <h3 className="text-2xl font-semibold mb-4">My Journey</h3>
            <div className="space-y-4 text-muted-foreground">
              <p>
              Computer Science graduate and developer passionate about Generative AI, 
              Machine Learning, and backend engineering. With hands-on experience at IBM, 
              I’ve built and deployed RAG-based chat systems, autonomous LLM-driven code 
              agents, and cloud-native AI applications. 
              </p><p>My expertise spans Python, PyTorch,
               FastAPI, LangChain, and vector databases, enabling me to deliver scalable, 
               high-performance, and feedback-integrated AI solutions from concept to production.
              </p>
              
            </div>

            {/* Code snippet */}
            <div className="bg-card border border-border rounded-lg p-4 font-mono text-sm">
              <div className="text-muted-foreground mb-2">// Philosophy</div>
              <div className="text-foreground">
                <span className="text-primary">function</span>{' '}
                <span className="text-accent">buildAmazingThings</span>() {'{'}<br />
                &nbsp;&nbsp;<span className="text-primary">return</span>{' '}
                <span className="text-green-400">"Keep learning, keep building"</span>;<br />
                {'}'}
              </div>
            </div>
          </div>

          {/* Highlights */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {highlights.map((item) => (
              <Card key={item.title} className="p-4 card-elegant">
                <item.icon className="h-8 w-8 text-primary mb-3" />
                <h4 className="font-semibold mb-2">{item.title}</h4>
                <p className="text-sm text-muted-foreground">{item.description}</p>
              </Card>
            ))}
          </div>
        </div>

        {/* Skills */}
        <div className="space-y-8">
          <h3 className="text-2xl font-semibold text-center mb-8">
            Tech <span className="gradient-text">Stack</span>
          </h3>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center space-y-4">
              <h4 className="text-lg font-semibold text-primary">Frontend</h4>
              <div className="flex flex-wrap justify-center gap-2">
                {skills.frontend.map((skill) => (
                  <Badge key={skill} variant="secondary">
                    {skill}
                  </Badge>
                ))}
              </div>
            </div>

            <div className="text-center space-y-4">
              <h4 className="text-lg font-semibold text-primary">Backend</h4>
              <div className="flex flex-wrap justify-center gap-2">
                {skills.backend.map((skill) => (
                  <Badge key={skill} variant="secondary">
                    {skill}
                  </Badge>
                ))}
              </div>
            </div>

            <div className="text-center space-y-4">
              <h4 className="text-lg font-semibold text-primary">Tools</h4>
              <div className="flex flex-wrap justify-center gap-2">
                {skills.tools.map((skill) => (
                  <Badge key={skill} variant="secondary">
                    {skill}
                  </Badge>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;