from __future__ import annotations
from typing import List  # <-- List is defined in the module's global scope
from pydantic import BaseModel


def this_works():
    class Model(BaseModel):
        a: List[int]

    print(Model(a=(1, 2)))
    
    
    
 """
 This will break
 """

from __future__ import annotations
from pydantic import BaseModel


def this_is_broken():
    # List is defined inside the function so is not in the module's
    # global scope!
    from typing import List

    class Model(BaseModel):
        a: List[int]

    print(Model(a=(1, 2)))
