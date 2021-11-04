from model import build_model
from utils import get_dataset
import logging

logger = logging.getLogger(__name__)


class trainer(object):
    def __init__(self, args):
        self.epoch = args.num_train_epochs
        self.output_size = args.output_size
        self.BS = args.train_batch_size
        self.args = args

    def train(self):

        logger.info("Loading the data ...")
        x_train, x_val, x_test, y_train, y_val, y_test = get_dataset(self.args.data_dir)
        input_shape = (x_train.shape[1], x_train.shape[2], 1)  # segments, coefficient, channel

        # build the model
        logger.info("Building the model ...")
        model = build_model(input_shape, self.output_size)

        # train the model
        logger.info("Training the model ...")
        model.fit(x_train, y_train, epochs=self.epoch, batch_size=self.BS, validation_data=(x_val, y_val))

        # evaluate the model
        test_error, test_acc = model.evaluate(x_test, y_test)
        logger.info(f"\nTEST ERROR: {test_error}, TEST ACC: {test_acc}")

        model.save(self.args.model_dir)
        logger.info("Saving model checkpoint to %s", self.args.model_dir)