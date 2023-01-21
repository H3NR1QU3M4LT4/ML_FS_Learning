import pytorch_lightning as pl
from model import LitAutoEncoder, Encoder, Decoder
from data import train_loader


def train():
    # model
    autoencoder = LitAutoEncoder(Encoder(), Decoder())

    # train model
    trainer = pl.Trainer()
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)