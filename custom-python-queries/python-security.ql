import python

from Call call
where
  call.getCallee() instanceof AttributeAccess and
  call.getCallee().(AttributeAccess).getAttr() = "load" and
  call.getCallee().(AttributeAccess).getBase() instanceof Name and
  call.getCallee().(AttributeAccess).getBase().(Name).getId() = "pickle"
select call, "Use of pickle.load detected, potential A08: Software and Data Integrity Failure (insecure deserialization)."