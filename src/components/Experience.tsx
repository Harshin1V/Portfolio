import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';

const Experience = () => {
  const experiences = [
    {
      id: 1,
      title: 'Senior Full Stack Developer',
      company: 'Tech Innovations Inc.',
      period: '2022 - Present',
      location: 'Remote',
      description: 'Lead development of scalable web applications using React, Node.js, and cloud technologies. Mentored junior developers and architected microservices solutions.',
      technologies: ['React', 'Node.js', 'AWS', 'Docker', 'TypeScript'],
      achievements: [
        'Increased application performance by 40%',
        'Led team of 5 developers',
        'Implemented CI/CD pipeline reducing deployment time by 60%'
      ]
    },
    {
      id: 2,
      title: 'Full Stack Developer',
      company: 'Digital Solutions Co.',
      period: '2020 - 2022',
      location: 'San Francisco, CA',
      description: 'Developed and maintained multiple client projects using modern web technologies. Collaborated with design teams to implement pixel-perfect UIs.',
      technologies: ['Vue.js', 'Express', 'MongoDB', 'Redis', 'SCSS'],
      achievements: [
        'Delivered 15+ successful projects',
        'Improved client satisfaction by 25%',
        'Established coding standards and best practices'
      ]
    },
    {
      id: 3,
      title: 'Frontend Developer',
      company: 'StartupXYZ',
      period: '2019 - 2020',
      location: 'New York, NY',
      description: 'Built responsive web applications and collaborated with product team to define user requirements. Focused on creating exceptional user experiences.',
      technologies: ['React', 'JavaScript', 'Sass', 'Webpack', 'Jest'],
      achievements: [
        'Reduced page load time by 50%',
        'Increased user engagement by 30%',
        'Implemented comprehensive testing suite'
      ]
    }
  ];

  const education = [
    {
      degree: 'Bachelor of Science in Computer Science',
      school: 'University of Technology',
      period: '2015 - 2019',
      description: 'Graduated Magna Cum Laude. Focused on software engineering, algorithms, and web development.'
    }
  ];

  return (
    <section id="experience" className="py-20 px-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Work <span className="gradient-text">Experience</span>
          </h2>
          <p className="text-lg text-muted-foreground">
            My professional journey in software development
          </p>
        </div>

        {/* Experience Timeline */}
        <div className="space-y-8 mb-16">
          {experiences.map((exp, index) => (
            <div key={exp.id} className="relative">
              {/* Timeline line */}
              {index !== experiences.length - 1 && (
                <div className="absolute left-4 top-16 bottom-0 w-0.5 bg-border"></div>
              )}
              
              {/* Timeline dot */}
              <div className="absolute left-2 top-6 w-4 h-4 bg-primary rounded-full border-4 border-background"></div>
              
              {/* Content */}
              <Card className="ml-12 p-6 card-elegant">
                <div className="space-y-4">
                  {/* Header */}
                  <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2">
                    <div>
                      <h3 className="text-xl font-semibold">{exp.title}</h3>
                      <p className="text-primary font-medium">{exp.company}</p>
                    </div>
                    <div className="text-sm text-muted-foreground">
                      <div>{exp.period}</div>
                      <div>{exp.location}</div>
                    </div>
                  </div>

                  {/* Description */}
                  <p className="text-muted-foreground">{exp.description}</p>

                  {/* Technologies */}
                  <div className="flex flex-wrap gap-2">
                    {exp.technologies.map((tech) => (
                      <Badge key={tech} variant="secondary">
                        {tech}
                      </Badge>
                    ))}
                  </div>

                  {/* Achievements */}
                  <div>
                    <h4 className="font-medium mb-2">Key Achievements:</h4>
                    <ul className="list-disc list-inside text-sm text-muted-foreground space-y-1">
                      {exp.achievements.map((achievement, i) => (
                        <li key={i}>{achievement}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </Card>
            </div>
          ))}
        </div>

        {/* Education */}
        <div>
          <h3 className="text-2xl font-semibold mb-8 text-center">
            <span className="gradient-text">Education</span>
          </h3>
          
          {education.map((edu, index) => (
            <Card key={index} className="p-6 card-elegant">
              <div className="space-y-2">
                <h4 className="text-lg font-semibold">{edu.degree}</h4>
                <p className="text-primary font-medium">{edu.school}</p>
                <p className="text-sm text-muted-foreground">{edu.period}</p>
                <p className="text-muted-foreground">{edu.description}</p>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Experience;