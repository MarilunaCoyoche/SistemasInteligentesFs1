package Views;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ViewPreferences extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			ViewPreferences dialog = new ViewPreferences();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(false);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public ViewPreferences() {
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setLayout(new FlowLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton btnRetroceder = new JButton("Retroceder");
				btnRetroceder.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						ViewPhysicalActivity view = new ViewPhysicalActivity();
						contentPanel.setVisible(false);
						view.setVisible(true);
					}
				});
				btnRetroceder.setActionCommand("Retroceder");
				buttonPane.add(btnRetroceder);
				getRootPane().setDefaultButton(btnRetroceder);
			}
			{
				JButton btnContinuar = new JButton("Continuar");
				btnContinuar.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						ViewMainMenu view = new ViewMainMenu();
						contentPanel.setVisible(false);
						view.getFrame().setVisible(true);
					}
				});
				btnContinuar.setActionCommand("Continuar");
				buttonPane.add(btnContinuar);
			}
		}
	}

}
