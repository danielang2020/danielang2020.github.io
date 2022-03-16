# Domain Driven Design Quickly
## 1. What Is Domain-Driven Design  
> When we begin a software project, we should focus on the domain it is operating in. The entire purpose of the software is to enhance a specific domain. To be able to do that, the software has to fit harmoniously with the domain it has been created for. Otherwise it will introduce strain into the domain, provoking malfunction, damage, and even wreak chaos.  

> The best way to do it is to make software a reflection of the domain. Software needs to incorporate the core concepts and elements of the domain, and to precisely realize the relationships between them. Software has to model the domain.  

> Software which does not have its roots planted deeply into the domain will not react well to change over time.  

> There are different approaches to software design.  
>- One is the waterfall design method. This method involves a number of stages. The business experts put up a set of requirements which are communicated to the business analysts. The analysts create a model based on those requirements, and pass the results to the developers, who start coding based on what they have received. It's a one way flow of knowledge. While this has been a traditional approach in software design, and has been used with a certain level of success over the years, it has flaws and limits. The main problem is that there is no feedback from the analysts to the business experts or from the developers to the analysts.  
>- Another approach is the Agile methodologies, such as Extreme Programming(XP). These mehodologies are a collective movement against the waterfall approach, resulting from the difficulties of trying to come up with all the requirements upfront, particularly in light of requirements change. It's really hard to create a complete model which covers all aspects of a domain upfront. It takes a lot of thinking, and often you just cann't see all the issue involved from the beginning, nor can you foresee some of the nagative side effects or mistakes of your design. Another problem Agile attempts to solve is the so called "analysis paralysis", with team members so afraid of making any design decisions that they make no progress at all. While Agile advocates recognize the imporance of design decision, they resist upfront design. Instead they employ a great deal of implementation flexibility, and through iterative development with continuous business stakeholder participation and a lot of refactoring, the development team gets to learn more about the customer domain and can better produce software that meets the customers needs.

## 2. The ubiquitous Language
### The Need for a Common Language
> A project faces serious problems when team members don't share a common language for discussing the domain. Domain experts use their jargon while technical team members have their own language tuned for discussing the domain in terms of design.  

### Creating the Ubiquitous Language
> We can use documents. One advisable way of communicating the model is to make some small diagrams each containing a subset of the model.

## 3. MODEL-DRIVEN DESIGN
> Any domain can be expressed with many models, and any model can be expressed in various ways in code. For each particular problem there can be more than one solution. It is important to choose a model which can be easily and accurately put into code.  

> Those who write the code should know the model very well, and should feel responsible for its integrity. They should realize that a change to the code implies a change to the model.  

> Any technical person contributing to the model must spend some time touching the code, whatever primary role he or she plays on the project. Anyone responsible for changing code must learn to express a model through the code. Every developer must be involved in some level of discussion about the model and have contact with domain experts. Those who contribute in different ways must consciously engage those who touch the code in a dynamic exchange of model ideas through the Ubiquitous Language.

> Design a portion of the software system to reflect the domain model in a very literal way, so that mapping is obvious.  

> Object-oriented programming is suitable for model implementation because they are both based on the same paradigm.

### The Building Blocks Of A Model-Driven Design
![](img/p.png)

>- 
