import python
from Call call
where call.getFunction().(Name).getId() = "load" and
      call.getFunction().getQualifier().(Name).getId() = "pickle"
select call, "Use of pickle.load detected, potential A08: Software and Data Integrity Failure (insecure deserialization)."