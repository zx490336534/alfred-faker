import os
import sys

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

from vendor.faker import Faker

faker = Faker(locale='zh_CN')

fakeType = sys.argv[1]
fakeValue = getattr(faker, fakeType)()

print(fakeValue)
