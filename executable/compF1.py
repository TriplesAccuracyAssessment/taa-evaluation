 #
 # (C) Copyright 2017 Shuangyan Liu
 # Shuangyan.Liu@open.ac.uk 
 # Knowledge Media Institute
 # The Open University, United Kingdom
 # 
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 #

# requires Python2
from sklearn.metrics import precision_recall_fscore_support
import sys
import ast

# arg1: list containing human assessed labels
arg1 = ast.literal_eval(sys.argv[1])
# arg2: list containing predicted labels
arg2 = ast.literal_eval(sys.argv[2])
metrics = precision_recall_fscore_support(arg1, arg2, average='binary')
f = -metrics[2]
print f
