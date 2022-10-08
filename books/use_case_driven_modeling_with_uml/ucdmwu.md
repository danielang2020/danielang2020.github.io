1. 产品负责编写用户故事。（user story）
2. 开发负责梳理故事中的名词和动词，汇总去重。
3. 开发与产品确认汇总去重后的词库，保证理解一致。
4. 确认词库中每一个词语对应的英文，保证理解一致。（gloosary）
5. 开发根据词库中的名词，不包含具体属性及方法，结合多态is-a和聚合has-a关系编写静态域模型。（model domain）
    a. Focus on real-world (problem domain) objects.  
    b. Use generalization (is-a) and aggregation (has-a) relationships to show how the objects relate to each other.
    c. Limit your initial domain modeling efforts to a couple of hours.  
    d. Organize your classes around key abstractions in the problem domain.
    e. Don’t mistake your domain model for a data model.
    f. Don’t confuse an object (which represents a single instance) with a database table (which contains a collection of things).
    g. Use the domain model as a project glossary.
    h. Do your initial domain model before you write your use cases, to avoid name ambiguity.
    i. Don’t expect your final class diagrams to precisely match your domain model, but there should be some resemblance between them.
    j. Don’t put screens and other GUI-specific classes on your domain model.
6. 开发根据词库中的动词编写动态使用用例，包括：成功场景、失败场景及对应处理方法。（uml use case）
7. 5到6步骤会反复执行。使用用例是在域模型范围内进行编写，随着使用用例的扩展，可能存在域模型无法满足，此时需要调整域模型以适应使用用例。
8. 与产品确认使用用例，保证理解一致。
9. 开发编写动态时序图。（uml sequence diagram）
10. 与产品确认时序图，保证理解一致。
11. 7到9步骤会反复执行。
12. 通过 域模型 + 时序图 保证产品、开发和测试理解一致。
13. 开发根据静态域模型编写静态类图。（uml class diagram）
14. 测试根据动态使用用例和时序图编写测试用例。（test case）
15. 开发通过静态类图进行Clean Architecture编码及附带单元测试。（code + unit test）
16. 考虑数据存储形式。（DBMS/NoSQL）
17. 开发考虑协议及提供对外接口文档。（RESTful API / RPC / Websocket）
18. 测试根据对外接口文档结合测试用例编写业务流程测试脚本。（postman + mock）
19. 前端使用测试提供的脚本对接后台mock服务。
20. 通过 接口文档 + 业务测试脚本 + 前端对接mock服务 保证开发、测试和前端理解一致。

> ![](img/ICONIX.png)