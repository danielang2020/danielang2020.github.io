# Designing Data-Intensive Applications

## CHAPTER 1 Reliable, Scalable, and Maintainable Applications
> When building an application, we still need to figure out which tools and which approaches are the most appropriate for the task at hand.

## CHAPTER 2 Data Models and Query Languages
### Relational Versus Document Database Today
> The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some application it is closer to the data structures used by the application(one-to-many). The relational model counters by providing better support for joins, and many-to-one and many-to-many relationships.

> It's not possible to say in general which data model leads to simpler application code; it depends on the kinds of relationships that exist between data items. For highly interconnected data, the document model is awkward, the relational model is acceptable, and graph models are the natural.

### MapReduce Querying
![](img/mr.png)

49