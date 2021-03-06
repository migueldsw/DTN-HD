"""
DTN
"""
import keras
from keras.layers import Input, Dense
from keras.models import Model


class SSDTN(object):
    """
    SS DTN
    """

    def __init__(self, num_class=10):
        text_input = Input(shape=(1000,), name='text_input')
        img_input = Input(shape=(1226,), name='img_input')

        # SAEs
        text_enc = Dense(512, activation='sigmoid', name='txt_dens_1')(text_input)
        text_enc = Dense(128, activation='sigmoid', name='txt_dens_2')(text_enc)

        img_enc = Dense(618, activation='sigmoid', name='img_dens_1')(img_input)
        img_enc = Dense(128, activation='sigmoid', name='img_dens_2')(img_enc)

        net = keras.layers.concatenate([text_enc, img_enc])
        net = Dense(512, activation='sigmoid', name='s_shared_dens_1')(net)
        net = Dense(120, activation='sigmoid', name='s_shared_dens_2')(net)

        output = Dense(num_class, activation='sigmoid', name='output')(net)

        self.model = Model(inputs=[img_input, text_input], outputs=[output])
        self.model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

        self.history_list = []
        self.metrics_list = []

    def train(self, x_img, x_txt, y, epoch=200):
        history = self.model.fit({'text_input': x_txt, 'img_input': x_img},
                                 {'output': y},
                                 epochs=epoch,
                                 verbose=1,
                                 batch_size=1)

        self.history_list.append(history)

    def eval(self, x_img, x_txt, y):
        metrics = self.model.evaluate(
            {'text_input': x_txt, 'img_input': x_img},
            {'output': y},
            verbose=1,
            batch_size=1)
        self.metrics_list.append(metrics)

    def check(self):
        print "input"
        print self.model.input[0].shape
        print self.model.input[1].shape
        print "output"
        print self.model.output.shape
        print "layers"
        for l in self.model.layers:
            print "   " + l.get_config()['name']
            if 'units' in l.get_config():
                print "        " + str(l.get_config()['units'])
            print "        layer shape:"
            for w in l.get_weights():
                print "            " + str(w.shape)

                # txtd1 = self.model.get_layer(name='txt_dens_1').get_weights()
                # print len(txtd1[0]), len(txtd1[1])
                # print txtd1[0].shape, txtd1[1].shape
                # print txtd1[1][40]


if __name__ == "__main__":
    dtn = SSDTN()
    dtn.check()
