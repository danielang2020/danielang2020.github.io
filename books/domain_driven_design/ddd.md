# Domain-Driven Design
## Chapter Three. Binding Model and Implementation
### Model-Driven Design
> Model-Driven Design sets aside purely technical issues, each object in the design plays a conceptual role described in the model.    

### Hands-On Modelers
> Domain-Driven design puts a model to work to solve problems for an application. Through knowlodge crunching, a team distills a torrent of chaotic information into a practical model. A Model-Driven Design intimately connects the model and the implementation. The Ubiquitous language is the channel for all that information to flow between developers, domain experts, and the software.  

## Chapter Four. Isolating the Domain
### Layered Architecture
> When the domain-related code is diffused through such a large amount of other code, it becomes extremely difficult to see and to reason about. Superficial changes to the UI can actually change business logic. To change a business rule may require meticulous tracing of UI code, database code, or other program elements. Implementing coherent, model-driven objects becomes impractical. Automated testing is awkward. With all the technologies and logic involved in each activity, a program must be kept very simple or it becomes impossible to understand.  

### The Domain Layer is Where the Model Lives
> Domain-driven design requires only one particular layer to exist. The domain model is a set of concept. The "Domain layer" is the manifestation of the model and all directly related design elements.   

> Isolating the domain implementation is a prerequisite for domain-driven design.  

## Chapter Five. A Model Expressed in Software
> A Service is something that is done for a client on request. In the technical layers of the software, there are  many Services. They emerge in the domain also, when some activity is modeled that corresponds to something the software must do, but does not correspond with state.  

> In a MODEL-DRIVEN-DESIGN, MODULES are part of the model, and they should reflect concepts in the domain.  

### Association
> When application requirements do not call for traversal in both directions, adding a traversal direction reduces interdependence and simplifies the design.  

> Constraining the traversal direction of a many-to-many association effectively reduces its implementation to one-to-many -- a much easier design.  

### Entities(a.k.a. Reference Object)
> Many objects are not fundamentally defined by their attributes, but rather by a thread of continuity and identity.  

### Value Objects
> VALUE OBJECTs are instantiated to represent elements of the design that we care about only for what they are, not who or which they are.  

> As long as a VALUE OBJECT is immutable, change management is simple - there isn't any change except full replacement. Immutable objects can be freely shared.   

> If a VALUE's implementation is to be mutable, then it must not be shared. Whether you will be sharing or not, design VALUE OBJECT as immutable when you can.  

> If the value of an attribute changes, you use a different VALUE OBJECT, rather than modifying the existing one.  
>```
> public class Address{
>    private String name;
>
>    public Address(String name){
>        this.name = name;
>    }
>
>    public Address changeName(String newName){
>        return new Address(newName);
>    }
> }
>```

### Services
> They have no state of their own nor any meaning in the domain beyond the operation they host. Still, at least this solution gives these distinct behaviors a home without messing up a real model object.    

> A SERVICE is an operation offered as an interface that stands alone in the model, without encapsulating state, as ENTITIES and VALUE OBJECTS do.   

### Modules(a.k.a. Package)
> Modules can look at detail within a MODULE without being overwhelmed by the whole, or they can look at relationships between MODULES in views that exclude interior detail.   

## Chapter Six. The Life Cycle of a Domain Object
### Aggregates
> An AGGREGATE is a cluster of associated objects that we treat as a unit of for the purpose of data changes. Each AGGREGATE has a root and a boundary. The boundary defines what is inside the AGGREGATE. The root is a single, specific ENTITY contained in the AGGREGATE. The root is the only member of the AGGREGATE that outside objects are allowed to hold references to, although objects within the boundary may hold references to each other. ENTITIES other than the root have local identity, but that identity needs to be distinguishable only within the AGGREGATE, because no outside object can ever see it out of the context of the root ENTITY.  

### Factories
> Each creation method is atomic and enforces all invariants of the created object or AGGREGATE. A FACTORY should only be able to produce an object in a consistent state. For an ENTITY, this means the creation of the entire AGGREGATE, with all invariants satisfied, but probably with optional elements still to be added. For an immutable VALUE OBJECT, this means that all attributes are initialized to their correct final state. If the interface makes it possible to request an object that can't be created correctly, then an exception should be raised or some other mechanism should be invoked that will ensure that no improper return value is possible.   

> Avoiding calling constructors within constructors of other classes. Constructors should be dead simple. Complex assembles, especially of AGGREGATES, call for FACTORIES.   

> ENTITY FACTORIES differ from VALUE OBJECT FACTORIES in two ways. VALUE OBJECTS are Immutable; the product comes out complete in its final form. So the FACTORY operations have to allow for a full description of the product. ENTITY FACTORIES tend to take just the essential attributes required to make a valid AGGREGATE. Details can be added later if they are not required by an invariant.   

### Repositories
> The ideal is to hide all the inner workings from the client, so that client code will be the same whether the data is stored in an object database, stored in a relational database, or simply held in memory. The REPOSITORY will delegate to the appropriate infrastructure services to get the job done.    

> Encapsulating the mechanisms of storage, retrieval, and query is the most basic feature of a REPOSITORY implementation.   

> Although the REPOSITORY will insert into and delete from the database, it will ordinarily not commit anything. It is tempting to commit after saving, for example, but the client presumably has the context to correctly initiate and commit units of works.   

> Transaction management will be simpler if the REPOSITORY keeps its hands off.   

> FACTORIES and REPOSITORIES have distinct responsibilities. The FACTORY makes new objects; the REPOSITORY finds old objects.   

### Designing Objects for Relational Databases
> Technically, the relational table design does not have to reflect the domain model.  

## Chapter Seven. Using the Language: An Extended Example
> VALUE OBJECTS usually shouldn't reference their owners.  

## Chapter Fourteen. Maintaining Model Integrity  
> A model is meaningless unless it is logically consistent. In an ideal world, we would have a single model spanning the whole domain of the enterprise. This model would be unified, without any contradictory or overlapping definitions of terms. Every logical statement about the domain would be consistent.  

### Bounded Context
> Explicitly define the context within which a model applies. Explicitly set boundaries in terms of team organization, usage within specific parts of the appliction, and physical manifestions such as code bases and database schemas. Keep the model strictly consistent within these bounds, but don't be distracted or confused by issues outside.  



