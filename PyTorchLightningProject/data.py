from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision import transforms

dataset = MNIST(os.getcwd(), download=True, transform=transforms.ToTensor())
train_loader = DataLoader(dataset)