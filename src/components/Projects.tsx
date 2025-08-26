import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { ExternalLink, Github, Star, Zap, Users, TrendingUp } from 'lucide-react';

const Projects = () => {
  const projects = [
    {
      id: 1,
      title: 'E-Commerce Platform',
      description: 'Full-stack e-commerce solution with React, Node.js, and Stripe integration. Features include product catalog, shopping cart, user authentication, and comprehensive admin dashboard with analytics.',
      image: 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&q=80&w=800',
      technologies: ['React', 'Node.js', 'MongoDB', 'Stripe', 'Redis'],
      github: 'https://github.com',
      live: 'https://demo.com',
      featured: true,
      stats: { stars: 245, users: '12k+', performance: '99%' }
    },
    {
      id: 2,
      title: 'AI Task Management',
      description: 'Collaborative task management application with AI-powered prioritization, real-time updates, drag-and-drop functionality, and advanced team collaboration features with smart notifications.',
      image: 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?auto=format&fit=crop&q=80&w=800',
      technologies: ['Vue.js', 'Express', 'Socket.io', 'TensorFlow', 'PostgreSQL'],
      github: 'https://github.com',
      live: 'https://demo.com',
      featured: true,
      stats: { stars: 189, users: '8k+', performance: '97%' }
    },
    {
      id: 3,
      title: 'Analytics Dashboard',
      description: 'Beautiful real-time analytics dashboard with interactive charts, location-based insights, and comprehensive weather data visualization.',
      image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800',
      technologies: ['Next.js', 'TypeScript', 'D3.js', 'Charts.js'],
      github: 'https://github.com',
      live: 'https://demo.com',
      featured: false,
      stats: { stars: 156, users: '5k+', performance: '95%' }
    },
    {
      id: 4,
      title: 'AI Chat Assistant',
      description: 'Intelligent chat assistant powered by OpenAI API with context awareness, conversation memory, and advanced natural language processing.',
      image: 'https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800',
      technologies: ['React', 'OpenAI API', 'Node.js', 'Redis'],
      github: 'https://github.com',
      live: 'https://demo.com',
      featured: false,
      stats: { stars: 203, users: '6k+', performance: '98%' }
    }
  ];

  const featuredProjects = projects.filter(p => p.featured);
  const otherProjects = projects.filter(p => !p.featured);

  return (
    <section id="projects" className="py-20 px-4 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-primary/5 rounded-full blur-3xl floating-element"></div>
      <div className="absolute bottom-0 right-1/4 w-72 h-72 bg-accent/5 rounded-full blur-3xl floating-element" style={{ animationDelay: '2s' }}></div>
      
      <div className="max-w-7xl mx-auto relative z-10">
        <div className="text-center mb-16">
          <Badge variant="outline" className="mb-6 px-4 py-2 text-sm font-medium">
            Portfolio
          </Badge>
          <h2 className="text-4xl md:text-6xl font-bold mb-6">
            Featured <span className="gradient-text">Projects</span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            A collection of projects that showcase my skills in full-stack development,
            UI/UX design, and modern web technologies with real-world impact.
          </p>
        </div>

        {/* Featured Projects */}
        <div className="space-y-20 mb-20">
          {featuredProjects.map((project, index) => (
            <div
              key={project.id}
              className={`grid lg:grid-cols-2 gap-12 items-center ${
                index % 2 === 1 ? 'lg:direction-rtl' : ''
              }`}
            >
              {/* Project Image */}
              <div className={`${index % 2 === 1 ? 'lg:order-2' : ''}`}>
                <div className="relative group card-hover">
                  <div className="card-elegant overflow-hidden">
                    <img
                      src={project.image}
                      alt={project.title}
                      className="w-full h-80 object-cover transition-transform duration-700 group-hover:scale-110"
                    />
                    
                    {/* Featured badge */}
                    <div className="absolute top-6 left-6">
                      <Badge className="bg-primary text-primary-foreground px-3 py-1 text-xs font-semibold">
                        ⭐ Featured
                      </Badge>
                    </div>
                    
                    {/* Hover overlay */}
                    <div className="absolute inset-0 bg-background/90 opacity-0 group-hover:opacity-100 transition-all duration-500 flex items-center justify-center">
                      <div className="flex space-x-4">
                        <Button variant="outline" size="lg" className="magnetic-hover">
                          <ExternalLink className="h-5 w-5 mr-2" />
                          Live Demo
                        </Button>
                        <Button size="lg" className="glow-effect magnetic-hover">
                          <Github className="h-5 w-5 mr-2" />
                          View Code
                        </Button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Project Info */}
              <div className={`space-y-6 ${index % 2 === 1 ? 'lg:order-1' : ''}`}>
                <div className="flex items-center justify-between">
                  <h3 className="text-3xl md:text-4xl font-bold gradient-text">{project.title}</h3>
                  
                  {/* Project Stats */}
                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <div className="flex items-center gap-1">
                      <Star className="w-4 h-4 text-accent" />
                      <span>{project.stats.stars}</span>
                    </div>
                    <div className="flex items-center gap-1">
                      <Users className="w-4 h-4 text-primary" />
                      <span>{project.stats.users}</span>
                    </div>
                  </div>
                </div>
                
                <p className="text-lg text-muted-foreground leading-relaxed">{project.description}</p>
                
                <div className="flex flex-wrap gap-3">
                  {project.technologies.map((tech) => (
                    <Badge key={tech} variant="secondary" className="px-4 py-2 text-sm bg-muted hover:bg-muted-light magnetic-hover">
                      {tech}
                    </Badge>
                  ))}
                </div>

                <div className="flex space-x-4 pt-4">
                  <Button className="magnetic-hover glow-effect group" asChild>
                    <a href={project.live} target="_blank" rel="noopener noreferrer">
                      <ExternalLink className="mr-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                      Live Demo
                    </a>
                  </Button>
                  <Button variant="outline" className="magnetic-hover group" asChild>
                    <a href={project.github} target="_blank" rel="noopener noreferrer">
                      <Github className="mr-2 h-5 w-5 group-hover:rotate-12 transition-transform" />
                      View Code
                    </a>
                  </Button>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Other Projects */}
        <div>
          <div className="text-center mb-12">
            <h3 className="text-3xl md:text-4xl font-bold mb-4">More <span className="gradient-text-accent">Projects</span></h3>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Additional projects showcasing various technologies and creative solutions.
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 gap-8 stagger-animation">
            {otherProjects.map((project, index) => (
              <Card key={project.id} className="card-elegant card-hover group" style={{ '--index': index } as React.CSSProperties}>
                <div className="space-y-6 p-8">
                  <div className="flex justify-between items-start">
                    <h4 className="text-2xl font-bold group-hover:gradient-text transition-all duration-300">{project.title}</h4>
                    
                    {/* Project Stats - Mini */}
                    <div className="flex items-center gap-3 text-xs text-muted-foreground">
                      <div className="flex items-center gap-1">
                        <Star className="w-3 h-3 text-accent" />
                        <span>{project.stats.stars}</span>
                      </div>
                      <div className="flex items-center gap-1">
                        <TrendingUp className="w-3 h-3 text-primary" />
                        <span>{project.stats.performance}</span>
                      </div>
                    </div>
                  </div>
                  
                  <p className="text-muted-foreground leading-relaxed">{project.description}</p>
                  
                  <div className="flex flex-wrap gap-2">
                    {project.technologies.map((tech) => (
                      <Badge key={tech} variant="secondary" className="px-3 py-1 text-xs bg-muted hover:bg-muted-light magnetic-hover">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                  
                  <div className="flex justify-between pt-4 border-t border-border-light">
                    <Button variant="ghost" size="sm" className="magnetic-hover group" asChild>
                      <a href={project.live} target="_blank" rel="noopener noreferrer">
                        <ExternalLink className="h-4 w-4 mr-2 group-hover:translate-x-1 transition-transform" />
                        Live
                      </a>
                    </Button>
                    <Button variant="ghost" size="sm" className="magnetic-hover group" asChild>
                      <a href={project.github} target="_blank" rel="noopener noreferrer">
                        <Github className="h-4 w-4 mr-2 group-hover:rotate-12 transition-transform" />
                        Code
                      </a>
                    </Button>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>

        {/* View More Section */}
        <div className="text-center mt-20">
          <div className="card-elegant max-w-md mx-auto card-hover">
            <Zap className="w-16 h-16 text-primary mx-auto mb-6 pulse-glow" />
            <h3 className="text-3xl font-bold mb-4 gradient-text">Explore More</h3>
            <p className="text-muted-foreground mb-8 leading-relaxed">
              Discover additional projects and contributions on my GitHub profile.
            </p>
            <Button className="magnetic-hover glow-effect" asChild>
              <a href="https://github.com" target="_blank" rel="noopener noreferrer">
                <Github className="w-5 h-5 mr-2" />
                View All Projects
              </a>
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Projects;
