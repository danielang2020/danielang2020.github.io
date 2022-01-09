# Designing Data-Intensive Applications
![](img/db.png)

## CHAPTER 1 Reliable, Scalable, and Maintainable Applications
> When building an application, we still need to figure out which tools and which approaches are the most appropriate for the task at hand.

## CHAPTER 2 Data Models and Query Languages
### Relational Versus Document Database Today
> The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some application it is closer to the data structures used by the application(one-to-many). The relational model counters by providing better support for joins, and many-to-one and many-to-many relationships.

> It's not possible to say in general which data model leads to simpler application code; it depends on the kinds of relationships that exist between data items. For highly interconnected data, the document model is awkward, the relational model is acceptable, and graph models are the natural.

### MapReduce Querying
![](img/mr.png)

### Graph-Like Data Models
> If your application has mostly one-to-many relationships(tree-structured data) or no relationships between records, the document model is appropriate. The relational model can handle simple case of many-to-many relationships, but as the connections within your data become more complex, it becomes more natural to start modeling your data as a graph.

> There are several different, but related, ways of structuring and querying data in graphs, the properties graph model(implemented by neo4j, Titan, and InfiniteGraph) and the triple-store model(implemented by Datomic, AllegroGraph, and others).

#### Property Graphs
> In the property graph model, each vertex consists of:
>- A unique identifier
>- A set of outgoing edges
>- A set of incoming edges
>- A collection of properties(key-value pairs) 
> Each edge consists of:
>- A unique identifier
>- The vertex at which the edge starts(the tail vertex)
>- The vertex at which the edge ends(the head vertex)
>- A label to describe the kind of relationship between the two vertices
>- A collection of properties(key-value pairs)

> Some important aspects of this model are:
>1. Any vertex can have an edge connecting it with any other vertex.
>2. Given any vertex, you can efficiently find both its incoming and its outgoing edges, and thus traverse the graph.
>3. By using different labels for different kinds of relationships, you can store several different kinds of information in a single graph, while still maintaining a clean data model.

#### Graph Queries in SQL
> In a relational database, you usually know in advance which joins you need in your query. In a graph query, you may need to traverse a variable number of edges before you find vertex you're looking for that is, the number of joins is not fixed in advance.

#### Triple-Stores and SPARQL
> The triple-store model is mostly equivalent to the property graph model, using different words to describe the same idea.

> In a triple-store, all information is stored in the form of very simple three-part statements:(subject, predicate, object). For example, in the triple(Jim, likes, bananas), Jim is the subject, likes is the predicate(verb), and bananas is the object.

## CHAPTER 3 Storage and Retrieval


