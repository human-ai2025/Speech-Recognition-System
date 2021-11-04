import argparse
from train import trainer
from utils import init_logger, set_seed
from keyword_spotting import Keyword_Spotting_Service


def main(args):
    init_logger()
    set_seed(args)

    import logging
    logger = logging.getLogger(__name__)
    logger.info("Started ...")
    train_model = trainer(args)

    if args.do_train:
        train_model.train()

    if args.do_predict:
        kss = Keyword_Spotting_Service(args)

        # make a prediction
        keyword, index = kss.predict("../testing/test-down.wav", args)
        logger.info("The keyword is %s", keyword)
        logger.info("The index is %d", index)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--model_dir",
                        default=r"C:\\Users\\tarini.m\\Desktop\\SR\\api\\model_weights\\model_trial1.h5",
                        type=str, help="Path to save, load model")
    parser.add_argument("--data_dir", default="data.json", type=str, help="The input data dir")
    parser.add_argument('--output_size', type=int, default=31, help="random seed for initialization")
    parser.add_argument("--do_train", action="store_true", help="Whether to run training.")
    parser.add_argument("--do_predict", action="store_true", help="Whether to run prediction")
    parser.add_argument('--seed', type=int, default=1234, help="random seed for initialization")
    parser.add_argument("--train_batch_size", default=32, type=int, help="Batch size for training.")
    parser.add_argument("--samples_to_consider", default=22050, type=int, help="The samples to consider.")
    parser.add_argument("--learning_rate", default=0.001, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--num_train_epochs", default=10, type=int, help="Total number of training epochs to perform.")
    args = parser.parse_args()

    main(args)
