import matplotlib.pyplot as plt
import json

loss_file_path = "out/train_loss.json"

with open(loss_file_path, 'r') as file:
    train_loss = json.load(file)


# Creating the plot
plt.figure(figsize=(20, 12))

for epoch, losses in train_loss.items():
    plt.plot(losses, label=f'Epoch {epoch}')

plt.xlabel('Iterations (10)')
plt.ylabel('Training Loss')
plt.title('Training Loss per Epoch')
plt.legend()

# Saving the plot to a local file
file_path = 'loss_plot_tinystories.png'
plt.savefig(file_path)